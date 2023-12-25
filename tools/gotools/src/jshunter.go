package main

import (
    "fmt"
    "os"
    "bufio"
    "log"
    "net/http"
    "io"
    "sync"
    "regexp"
    "flag"
)

func sendRequest(urls <-chan string, wg *sync.WaitGroup){
    defer wg.Done()
   
    for url:= range urls{
        response, err := http.Get(url)
        if err != nil{
            fmt.Printf("Cannot Download %s: %s\n", url, err)
            return
        }
        defer response.Body.Close()
        
        filename := generateFileName(url)
        
        jsfile, err := os.Create(filename)
        if err != nil{
            fmt.Printf("Cannot save %s : %s\n", url, err)
            return
        }
        defer jsfile.Close()
        
        bytes, err := io.Copy(jsfile, response.Body)
        if err != nil{
            fmt.Printf("Cannot save %s : %s", filename, err)
            return
        }
        
        fmt.Printf("%s [%d] [%d]\n",url, response.StatusCode, bytes)
    }
}


func generateFileName(url string) string{
    url = regexp.MustCompile(`[^a-zA-Z0-9 ]+`).ReplaceAllString(url, "_")
    extension := url[len(url)-3:]

    if extension == "_js"{
        url = url[:len(url)-3]           
        url += ".js"
    }else{
        url += ".js"
    }
    return url
}

func main(){
    threads := flag.Int("n", 50, "# number of threads")
    flag.Parse()
    if len(os.Args) < 2{
        fmt.Println("Usage: ./jshunter <urls.txt>")
        fmt.Println("Usage: ./jshunter -n 10 <urls.txt>")
        return
    }

    file_path := string(os.Args[len(os.Args)-1])
    file, err := os.Open(file_path)
    
    if err != nil{
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)

    var urls []string

    for scanner.Scan(){
        urls = append(urls, scanner.Text())
    }

    maxConcurrency := *threads
    urlChan := make(chan string,len(urls))    
    var wg sync.WaitGroup
    
    for _, url := range urls{
        urlChan <- url   
    }
    close(urlChan)

    for i:=0;i<maxConcurrency;i++ {
        wg.Add(1)
        go sendRequest(urlChan, &wg)
    }

    wg.Wait()
    fmt.Println("All file downloaded")
}

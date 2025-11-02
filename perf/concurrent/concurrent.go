package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

var filename string = "../data.txt"
var topN int8 = 30

type word struct {
	Word  string
	Count int
}

func countWords(words []string, ch chan map[string]int) {
	wordMap := make(map[string]int)

	// Count occurances of each word
	for _, word := range words {
		_, exists := wordMap[word]

		if exists {
			wordMap[word] += 1
		} else {
			wordMap[word] = 1
		}
	}

	ch <- wordMap
}

func main() {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic(err)
	}

	// create the channel
	ch := make(chan map[string]int)

	text := string(data)
	words := strings.Split(text, " ")

	// chunk up the words and use goroutines to calculate
	go countWords(words[:len(words)/2], ch)
	go countWords(words[len(words)/2:], ch)

	// receive the words from the channel
	wordMap1, wordMap2 := <-ch, <-ch

	// sort the words by count descending
	var sorted []word
	for key, value := range wordMap1 {
		if wordMap2[key] >= 1 {
			newCount := value + wordMap2[key]
			sorted = append(sorted, word{Word: key, Count: newCount})
			continue
		}
		sorted = append(sorted, word{key, value})
	}

	sort.Slice(sorted, func(i, j int) bool {
		return sorted[i].Count > sorted[j].Count
	})

	for i := range topN {
		word := sorted[i]
		fmt.Printf("%v:%d\n", word.Word, word.Count)
	}
}

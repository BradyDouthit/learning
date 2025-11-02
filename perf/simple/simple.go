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

func main() {
	data, err := os.ReadFile(filename)

	if err != nil {
		panic(err)
	}

	text := string(data)
	words := strings.Split(text, " ")
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

	// sort the words by count descending
	var sorted []word
	for key, value := range wordMap {
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

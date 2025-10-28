import fs from "node:fs";

const filepath = "data.txt";
const topN = 30;

try {
  const data = fs.readFileSync(filepath, "utf8");
  const words = data.split(" ");

  const wordMap = new Map();

  // get counts for each word
  words.forEach((word) => {
    const mappedWord = wordMap.get(word);

    if (!mappedWord) {
      wordMap.set(word, 1);
      return;
    }

    wordMap.set(word, mappedWord + 1);
  });

  const sorted = Array.from(wordMap).sort((a, b) => {
    const aCount = a[1];
    const bCount = b[1];
    return bCount - aCount;
  });
  const topWords = sorted.slice(0, topN);

  topWords.forEach(([word, count]) => {
    console.log(`${word}: ${count}`);
  });
} catch (err) {
  console.error(err);
}

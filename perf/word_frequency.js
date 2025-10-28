import fs from "node:fs";

const filepath = "data.txt";

try {
  const data = fs.readFileSync(filepath, "utf8");
  console.log(data);
} catch (err) {
  console.error(err);
}

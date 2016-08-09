# Equation Converter for GitHub Flavored Markdown

You can convert markdown text into the one which equations can be drawn automatically.

# Usage
## 1. Write a Markdown file
We assume that you wrote a Markdown file like below and saved as `example.md`.

```md:example.md
$e^{i\theta} = cos\theta + i\sin\theta$
```

But the equation cannot be drawn by default.

## 2. Convert the file
Run a command to convert the file.

```
python3 converter.py example.md
```

This command converts equations surrounded by a pair of dollar signs ($), and saves into `example.converted.md`

```md:example.converted.md
![](https://latex.codecogs.com/gif.latex?e%5E%7Bi%5Ctheta%7D%20%3D%20cos%5Ctheta%20%2B%20i%5Csin%5Ctheta)
```

## 3. Equations can be drawn!
The equation can be drawn beautifully.

---

![](https://latex.codecogs.com/gif.latex?e%5E%7Bi%5Ctheta%7D%20%3D%20cos%5Ctheta%20%2B%20i%5Csin%5Ctheta)

---

# Restriction

This converter allows only one equation per line. You cannot write more than 2 equations in one line.

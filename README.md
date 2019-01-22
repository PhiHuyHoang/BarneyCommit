## Rice Bored

A small flask app that generates random commit messages from Barney - HIMYM quotes.

```
https://barneycommit.herokuapp.com/
```

## Command

```
git config --global alias.rice !"sh -c \"git commit -m '$(curl -s http://barneycommit.herokuapp.com)'\""
```

## Usage Example:
```
git add .
git rice
git push
```
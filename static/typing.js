document.addEventListener("DOMContentLoaded", function () {
  const output = document.getElementById("output");

  const mainText = "Hi, I'm Moshe and I like to blog about ";
  const words = ["programming", "food", "traveling around the world!"];
  let delay = 100;

  function typeText(text, callback) {
    let i = 0;
    function typeChar() {
      if (i < text.length) {
        output.textContent += text[i++];
        setTimeout(typeChar, delay);
      } else if (callback) {
        callback();
      }
    }
    typeChar();
  }

  function deleteText(count, callback) {
    function deleteChar() {
      if (count > 0) {
        output.textContent = output.textContent.slice(0, -1);
        count--;
        setTimeout(deleteChar, delay);
      } else if (callback) {
        callback();
      }
    }
    deleteChar();
  }

  function loopWords(index = 0) {
    // first write mainText only once
    if (index === 0) {
      output.textContent = "";  // clear before typing mainText
      typeText(mainText, () => {
        typeText(words[index], () => {
          deleteText(words[index].length, () => {
            loopWords((index + 1) % words.length);
          });
        });
      });
    } else {
      typeText(words[index], () => {
        deleteText(words[index].length, () => {
          loopWords((index + 1) % words.length);
        });
      });
    }
  }

  loopWords();
});

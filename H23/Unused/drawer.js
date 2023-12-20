document.onmouseup = document.onkeyup = document.onselectionchange = function() {
    document.getElementById('selectedText').value = window.getSelection().toString();
  };
  
  document.onkeydown = function(e) {
    if (e.keyCode >= 49 && e.keyCode <= 57) { // keys 1-9
      var color;
      switch(e.keyCode) {
        case 49: color = 'red'; break;
        case 50: color = 'blue'; break;
        case 51: color = 'green'; break;
        // add more colors for other number keys
      }
      highlightSelection(color);
    }
  };
  
  function highlightSelection(color) {
    var selection = window.getSelection().getRangeAt(0);
    var selectedText = selection.extractContents();
    var span = document.createElement('span');
    span.style.backgroundColor = color;
    span.appendChild(selectedText);
    selection.insertNode(span);
  }
  
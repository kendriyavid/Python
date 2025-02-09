
let string = "<h1>Heading</h1>\n <p>testing the dom traversal</p> \n <p>harshdeepsingh </p>"
// we have to traverse using stack
let varstring=""
let stack=[]

const parser = new DOMParser();
const doc = parser.parseFromString(htmlString, 'text/html');
function traverseDOM(node) {
    console.log(node.nodeName);
    for (let i = 0; i < node.childNodes.length; i++) {
      traverseDOM(node.childNodes[i]);
    }
  }

traverseDOM(doc.body)
//Author: Christian Eriksen 
//Script for livesearching with scrolling with arrow possible. 

var selected = 0;

function liveSearch() {
    /**
     * Show drop down list once user starts typing input in the search bar 
     */
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName("li");
    dropdown = document.getElementById("myDropdown");
    if (input.value.trim() != '') {
        dropdown.classList.add('show');
    } else {
        dropdown.classList.remove('show');
    }
    
        for (i = 0; i < li.length; i++) {
            a = li[i].getElementsByTagName("a")[0];
            if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
            } else {
            li[i].style.display = "none";
            }
        }
    
    
};


let nodes= [];
let input = document.getElementById('myInput');
input.oninput = function() {
    selected = 0;
    setTimeout(() => {
        nodes = []
        removeSelected();
        counter = 0
        document.getElementById('myDropdown').querySelectorAll('li a').forEach(node => {
            if (node.parentNode.style.display != 'none') {
                if (counter === 0) {
                    node.classList.add('selected');
                }
                counter ++;
                nodes.push(node);
        }});
        }, "300")
}
    
        

let inputArrowListner = document.getElementById('myInput')
inputArrowListner.addEventListener('keyup', function(e) {
    var key = e.key || e.keyCode
    if (key === 'ArrowUp') { // up
        select(nodes[selected - 1]);
    }
    if (key === 'ArrowDown') { // down
        select(nodes[selected + 1]);
    }
    if (key === 'Enter') {
        let subject = document.querySelector('.selected').id;
        getListings(subject)
    }
    e.preventDefault();
});

const clicked = (obj) => {
    select(obj);
    getListings(obj.innerHTML.trim());
}

function removeSelected() {
    let obj = document.querySelector('li a.selected') 
    if (obj) {
        obj.classList.remove('selected');
    }
}


function select(el) {
    var ul = document.querySelector('ul');
    var s = [].indexOf.call(nodes, el);
    if (s === -1) return;
    
    selected = s;
    
    var elHeight = $(el).height();
    var scrollTop = $(ul).scrollTop();
    var viewport = scrollTop + $(ul).height();
    var elOffset = elHeight * selected;
    
    //console.log('select', selected, ' viewport', viewport, ' elOffset', elOffset);
    if (elOffset < scrollTop || (elOffset + elHeight) > viewport)
        $(ul).scrollTop(elOffset); 
    
    document.querySelector('li a.selected').classList.remove('selected');
    el.classList.add('selected');
} 
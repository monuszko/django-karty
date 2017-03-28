
function createElement(tagName, attrs) {
    var elem = document.createElement(tagName);
    for (var attr in attrs) {
        elem.setAttribute(attr, attrs[attr]);
    }
    return elem; 
}


function clickHandler(evnt) {
    var restUri = evnt.currentTarget.dataset.restUri;
    if (restUri) {
        updatePage(restUri);
    }
}


function sortClickHandler(evnt) {
    for (var button of document.getElementsByClassName('sort')) {
        button.disabled = false;
        if (button == evnt.currentTarget) {
            button.disabled = true;
        }
    }
}


function updatePage(path){
    // http://127.0.0.1:8000/karty/api/menucards/?page=2
    //
    
    var xhr = new XMLHttpRequest();
    xhr.open('GET', path);
    xhr.setRequestHeader('Accept', 'application/json');
    xhr.send(null);

    xhr.onreadystatechange = function () {
        var DONE = 4;
        var OK = 200;
        if (xhr.readyState === DONE) {
            if (xhr.status ===  OK) {
                var parsed = JSON.parse(xhr.responseText);
                var pagenr = /page=([0-9]+)/.exec(path);
                pagenr ? pagenr = pagenr[1] : pagenr = 1;
                parsed['page'] = pagenr;
                insertJSON(parsed);
            }
            else {
                console.log('Error: ' + xhr.status);
            }
        }
    }
}


function insertJSON(json) {
    var ul = document.getElementById('menucards');
    var pagination_text = 'Page ' + json['page'] + ' of ' + ul.dataset.numPages;
    document.getElementById('pagination').innerHTML = pagination_text;

    while (ul.firstChild) {
        ul.removeChild(ul.firstChild);
    }
    // TODO: make sure there are no memory leaks

    for (var mcard of json['results']) {
        var li = document.createElement('li');

        var a = createElement('a', {'title': mcard['name'], 'href': mcard['url']})
        var link_text = document.createTextNode(mcard['name']);
        a.appendChild(link_text);
        li.appendChild(a);

        var remaining = ' (' + mcard['num_dishes'] + 
                ' dishes, modified: ' + mcard['mod_date'] + ')';
        remaining = document.createTextNode(remaining);
        li.appendChild(remaining);
        var p = document.createElement('p');
        p.appendChild(document.createTextNode(mcard['desc']));
        li.appendChild(p);

        ul.appendChild(li);
    }

    var prev = document.getElementById('prev-page');
    prev.disabled = true;
    if (json['previous']) {
        prev.disabled = false;
        prev.dataset.restUri = json['previous'];
    }
    var next = document.getElementById('next-page');
    next.disabled = true;
    if (json['next']) {
        next.disabled = false;
        next.dataset.restUri = json['next'];
    }

}


document.getElementById('normal-links').classList.add('hidden');
document.getElementById('xhr-links').classList.remove('hidden');

for (var link of document.getElementsByTagName('button')) {
    link.addEventListener('click', clickHandler);
}

for (var button of document.getElementsByClassName('sort')) {
    button.addEventListener('click', sortClickHandler);
}



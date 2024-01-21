fetch('notes.json?' + new Date().getTime())
.then(response => response.json())
.then(jsonData => {
    // 首先，将JSON数据按日期排序
    jsonData.sort((a, b) => new Date(a.date) - new Date(b.date));

    var container = document.getElementById('json-container');

    jsonData.forEach(function(item, index) {
        var div = document.createElement('div');
        div.className = 'container ' + (index % 2 === 0 ? 'left' : 'right');
        var entry = document.createElement('div');
        entry.className = 'entry';
        var year = new Date(item.date).getFullYear();
        entry.innerHTML = '<h2>Year: ' + year + '</h2><p>' + item.content + '</p>';
        div.appendChild(entry);
        container.appendChild(div);
    });
})
.catch(error => console.error('Error:', error));

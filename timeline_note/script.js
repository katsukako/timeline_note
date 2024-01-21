fetch('notes.json?' + new Date().getTime())
.then(response => response.json())
.then(jsonData => {
    // 首先，将JSON数据按日期排序
    jsonData.sort((a, b) => new Date(a.date) - new Date(b.date));

    var container = document.getElementById('json-container');

    jsonData.forEach(function(item) {
        var div = document.createElement('div');
        div.className = 'entry';
        
        // 提取年份
        var year = new Date(item.date).getFullYear();

        // 只显示年份和内容
        div.innerHTML = '<h2>Year: ' + year + '</h2><p>' + item.content + '</p>';
        container.appendChild(div);
    });
})
.catch(error => console.error('Error:', error));

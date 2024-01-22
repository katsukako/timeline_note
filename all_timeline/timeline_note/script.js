fetch('notes.json')
.then(response => response.json())
.then(jsonData => {
    jsonData.sort((a, b) => new Date(a.date) - new Date(b.date));
    var timeline = document.getElementById('json-container');

    jsonData.forEach(function(item, index) {
        // 创建外层的container div
        var containerDiv = document.createElement('div');
        containerDiv.className = 'container ' + (index % 2 === 0 ? 'left' : 'right');

        // 创建entry div
        var entryDiv = document.createElement('div');
        entryDiv.className = 'entry';
        var year = new Date(item.date).getFullYear();

        // 创建并处理tags
        var tagsSpan = item.tags.map(tag => `<span class="tag">${tag}</span>`).join(" ");

        // 设置entry div的内容
        entryDiv.innerHTML = '<h2>' + year + '</h2><p>' + item.content + '</p>' + tagsSpan;

        // 将entry div添加到container div
        containerDiv.appendChild(entryDiv);

        // 将container div添加到timeline
        timeline.appendChild(containerDiv);
    });
})
.catch(error => console.error('Error:', error));

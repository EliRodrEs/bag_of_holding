function toggleDetails(row) {
    let nextRow = row.nextElementSibling;
    if (nextRow && nextRow.classList.contains('details-row')) {
        nextRow.classList.toggle('hidden');
    }
}

const searchForItem = () => {
    const inputValue = document.getElementById('hs-table-with-pagination-search').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log(window.location.href)
    fetch(window.location.href, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ search_term: inputValue })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('results-table').innerHTML = data.html;
    });
}
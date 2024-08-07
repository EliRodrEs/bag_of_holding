function toggleDetails(row) {
    let nextRow = row.nextElementSibling;
    if (nextRow && nextRow.classList.contains('details-row')) {
        nextRow.classList.toggle('hidden');
    }
}

const searchForItem = () => {
    const inputValue = document.getElementById('hs-table-with-pagination-search').value
    console.log(inputValue)
}
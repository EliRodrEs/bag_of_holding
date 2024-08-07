function toggleDetails(row) {
    let nextRow = row.nextElementSibling;
    if (nextRow && nextRow.classList.contains('details-row')) {
        nextRow.classList.toggle('hidden');
    }
}

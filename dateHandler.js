function changeDate(e) {
    var date = e.target.value;
    var features = [];
    drawMap(view, features, date);
}
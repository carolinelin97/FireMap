function changeDate(e) {
    var date = e.target.value;
    features = [];
    getData(getFunction, date)
        .then(drawMap(view, features, date));

    // getData(getFunction, date)
    //     .then(changeGraphics(features));
}

// function changeGraphics(graphics){
//     var addEdits = {
//         addFeatures: graphics
//     };
//     require(["esri/Map",
//         "esri/views/MapView",], function (map, view){
//         view.map.layers.applyEdits(addEdits);
//     })
//
// }
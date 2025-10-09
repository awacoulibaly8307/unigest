window.onload = function () {
    // --- Graphique Patients ---
    var etuChart = new CanvasJS.Chart("chartEtu", {
        exportEnabled: true,
        animationEnabled: true,
        data: [{
            type: "pie",
            yValueFormatString: "#,##0\"%\"",
            indexLabel: "{label} ({y})",
            dataPoints: window.sexData  // injecté par Django
        }]
    });
    etuChart.render();
};
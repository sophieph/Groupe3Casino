// Get data of levels avg
let seriesAjax = $.ajax({
    url: '/levels-avg',
    type: 'POST',
    global: false,
    async: false,
    success: function (res) {
        result = jQuery.parseJSON(res);
        return result;
    }
}).responseText;

let series = jQuery.parseJSON(seriesAjax);

// Get profig avg by level
let winningAvgAjax = $.ajax({
    url: '/winnings-avg',
    type: 'POST',
    global: false,
    async: false,
    success: function (res) {
        result = jQuery.parseJSON(res);
        return result;
    }
}).responseText;

let winningAvg = jQuery.parseJSON(winningAvgAjax);
console.log(winningAvg.winning);

var data1 = {
    labels: ['Niveau 1', 'Niveau 2', 'Niveau 3'],
    datasets: [{
        label: 'Moyenne de niveau atteints',
        data: series.levels,
        backgroundColor: [
            "#DEB887",
            "#F4A460",
            "#2E8B57"
        ],
        borderColor: [
            "#CDA776",
            "#E39371",
            "#1D7A46"
        ],
        borderWidth: [1, 1, 1]
    }]
};

//options
var options1 = {
    responsive: true,
    title: {
        display: true,
        position: "top",
        text: "Moyenne de niveau atteints",
        fontSize: 18,
        fontColor: "#111"
    },
    legend: {
        display: true,
        position: "bottom",
        labels: {
            fontColor: "#333",
            fontSize: 16
        }
    }
};

var ctx = document.getElementById('levels').getContext('2d');
var chart1 = new Chart(ctx, {
    type: "doughnut",
    data: data1,
    options: options1
});

var profitData = {
    label: 'Gain moyen par niveau',
    data: winningAvg.winnings,
    backgroundColor: [
        'rgba(60, 99, 132, 0.6)',
        'rgba(150, 99, 132, 0.6)',
        'rgba(240, 99, 132, 0.6)'
      ],
      borderColor: [
        'rgba(60, 99, 132, 1)',
        'rgba(150, 99, 132, 1)',
        'rgba(210, 99, 132, 1)',
      ],
      borderWidth: 2,
      hoverBorderWidth: 0
};

// var profitOption =  {
//     responsive: true,
//     title: {
//         display: true,
//         position: "top",
//         text: "Moyenne de niveau atteints",
//         fontSize: 18,
//         fontColor: "#111"
//     },
//     legend: {
//         display: true,
//         position: "bottom",
//         labels: {
//             fontColor: "#333",
//             fontSize: 16
//         }
//     }
// };

var profit = document.getElementById('profit-level').getContext('2d');
var lineChart = new Chart(profit, {
    type: 'bar',
    data: {
        labels: ["Niveau 1", "Niveau 2", "Niveau 3"],
        datasets: [profitData]
      },
});
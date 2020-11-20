let url = window.location.href;
let name = url.replace('http://127.0.0.1:5000/dashboard/', '');

/** Victory avg by name */
let victoryAvgAjax = $.ajax({
    url: '/victory-avg/' + name ,
    type: 'POST',
    global: false,
    async: false,
    success: function (res) {
        result = jQuery.parseJSON(res);
        return result;
    }
}).responseText;
let victoryAvg = jQuery.parseJSON(victoryAvgAjax);

/** victory by level 1 */
let victory1Ajax = $.ajax({
    url: '/victory/1/' + name ,
    type: 'POST',
    global: false,
    async: false,
    success: function (res) {
        result = jQuery.parseJSON(res);
        return result;
    }
}).responseText;
let victory1 = jQuery.parseJSON(victory1Ajax);

/** victory by level 2 */
let victory2Ajax = $.ajax({
    url: '/victory/2/' + name ,
    type: 'POST',
    global: false,
    async: false,
    success: function (res) {
        result = jQuery.parseJSON(res);
        return result;
    }
}).responseText;
let victory2 = jQuery.parseJSON(victory2Ajax);

/** victory by level 3 */
let victory3Ajax = $.ajax({
    url: '/victory/3/' + name ,
    type: 'POST',
    global: false,
    async: false,
    success: function (res) {
        result = jQuery.parseJSON(res);
        return result;
    }
}).responseText;
let victory3 = jQuery.parseJSON(victory3Ajax);

/** CHART 1 */
var data = {
    labels: [
        "Gagné",
        "Perdu"
    ],
    datasets: [
        {
            data: victoryAvg.victory,
            backgroundColor: [
                "#FF6384",
                "#63FF84",
            ]
        }]
};
var victoryChart = document.getElementById('victory-name').getContext('2d');
var chart1 = new Chart(victoryChart, {
    type: 'pie',
    data: data,
});

/** CHART 2 */
var data2 = {
    labels: [
        "Gagné",
        "Perdu"
    ],
    datasets: [
        {
            data: victory1.victory,
            backgroundColor: [
                "#FF6384",
                "#63FF84",
            ]
        }]
};
var victory1Chart = document.getElementById('victory-lvl1').getContext('2d');
var chart2 = new Chart(victory1Chart, {
    type: 'pie',
    data: data2,
});




/** CHART 3 */
var data3 = {
    labels: [
        "Gagné",
        "Perdu"
    ],
    datasets: [
        {
            data: victory2.victory,
            backgroundColor: [
                "#FF6384",
                "#63FF84",
            ]
        }]
};
var victory2Chart = document.getElementById('victory-lvl2').getContext('2d');
var chart3 = new Chart(victory2Chart, {
    type: 'pie',
    data: data3,
});




/** CHART 2 */
var data3 = {
    labels: [
        "Gagné",
        "Perdu"
    ],
    datasets: [
        {
            data: victory3.victory,
            backgroundColor: [
                "#FF6384",
                "#63FF84",
            ]
        }]
};
var victory3Chart = document.getElementById('victory-lvl3').getContext('2d');
var chart4 = new Chart(victory3Chart, {
    type: 'pie',
    data: data3,
    options: {
        title: {
            display: true,
            text: '% victoire au niveau 3'
        }
    }
});


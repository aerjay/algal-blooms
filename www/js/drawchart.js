Chart.defaults.global.pointHitDetectionRadius = 1;

var customTooltips = function (tooltip) {
    // Tooltip Element
    var tooltipEl = document.getElementById('chartjs-tooltip');

    if (!tooltipEl) {
        tooltipEl = document.createElement('div');
        tooltipEl.id = 'chartjs-tooltip';
        tooltipEl.innerHTML = '<table></table>';
        this._chart.canvas.parentNode.appendChild(tooltipEl);
    }

    // Hide if no tooltip
    if (tooltip.opacity === 0) {
        tooltipEl.style.opacity = 0;
        return;
    }

    // Set caret Position
    tooltipEl.classList.remove('above', 'below', 'no-transform');
    if (tooltip.yAlign) {
        tooltipEl.classList.add(tooltip.yAlign);
    } else {
        tooltipEl.classList.add('no-transform');
    }

    function getBody(bodyItem) {
        return bodyItem.lines;
    }

    // Set Text
    if (tooltip.body) {
        var titleLines = tooltip.title || [];
        var bodyLines = tooltip.body.map(getBody);
        var innerHtml = '<thead>';

        titleLines.forEach(function (title) {
            //       innerHtml += '<tr><th>' + title + '</th></tr>';
        });
        innerHtml += '</thead><tbody>';

        bodyLines.forEach(function (body, i) {
            //  var colors = tooltip.labelColors[i];
            //  var style = 'background:' + colors.backgroundColor;
            //  style += '; border-color:' + colors.borderColor;
            //  style += '; border-width: 2px';
            // var span = '<span class="chartjs-tooltip-key" style="' + style + '"></span>';
            innerHtml += '<tr><td><img src="img/' + tooltip.title[0] + 'lakeerie.png" height=300px width=300px> </td></tr>';
        });
        innerHtml += '</tbody>';

        var tableRoot = tooltipEl.querySelector('table');
        tableRoot.innerHTML = innerHtml;
    }

    var positionY = this._chart.canvas.offsetTop;
    var positionX = this._chart.canvas.offsetLeft;

    // Display, position, and set styles for font
    tooltipEl.style.opacity = 1;
    tooltipEl.style.left = positionX + tooltip.caretX + 'px';
    tooltipEl.style.top = positionY + tooltip.caretY + 'px';
    tooltipEl.style.fontFamily = tooltip._bodyFontFamily;
    tooltipEl.style.fontSize = tooltip.bodyFontSize + 'px';
    tooltipEl.style.fontStyle = tooltip._bodyFontStyle;
    tooltipEl.style.padding = tooltip.yPadding + 'px ' + tooltip.xPadding + 'px';
};


var json = (function () {
    var json = null;
    $.ajax({
        'async': true,
        'global': false,
        'url': "algal-blooms/ratios_dates.json",
        'dataType': "json",
        'success': function (data) {
            json = data;
        }
    });
    return json;
})();

var lineChartData = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    labels: [dates],
    datasets: [{
        borderColor: "#5C755F",
        pointBackgroundColor: "#9C9F84",
        fill: false,
        pointRadius: 6,
        pointHoverRadius: 6,
        data: [
            randomScalingFactor(),
            randomScalingFactor(),
            randomScalingFactor(),
            randomScalingFactor(),
            randomScalingFactor(),
            randomScalingFactor(),
            randomScalingFactor()
        ]
        /*}, {
            label: 'My Second dataset',
            borderColor: window.chartColors.blue,
            pointBackgroundColor: window.chartColors.blue,
            fill: false,
            data: [
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor(),
                randomScalingFactor()
            ]*/
    }]
};

window.onload = function () {
    var chartEl = document.getElementById('chart');
    Chart.scaleService.updateScaleDefaults('linear', {
        ticks: {
            min: 0
        }
    });
    window.myLine = new Chart(chartEl, {
        type: 'line',
        data: lineChartData,
        options: {
            title: {
                display: true,
                //                text: 'Chart.js Line Chart - Custom Tooltips'
            },
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Ratio'
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }]
            },
            tooltips: {
                enabled: false,
                mode: 'index',
                position: 'nearest',
                custom: customTooltips
            }
        }
    });
};
// Setup block
const cpuUtilData = {
    labels: util_time_labels,
    datasets: [
        {
        label: 'CPU Utilization',
        // Chart Data
        data: cpu_util_data,
        backgroundColor: ['#3C87D5', ],
        borderColor: ['#3C87D5', ],
        pointRadius: 3,
        pointBackgroundColor: ['#3C87D5', ],
        pointBorderColor: ['#3C87D5', ],
        pointHoverRadius: 3,
        pointHoverBackgroundColor: ['#3C87D5', ],
        pointHoverBorderColor: ['#3C87D5', ],
        pointHitRadius: 10,
        pointBorderWidth: 2,
        }
    ]  // End datasets
};  // End data

// Legend Margin plugin block
const cpuUtilLegendMargin = {
    id: 'legendMargin',
    beforeInit(chart, legend, options){
        const fitValue = chart.legend.fit
        chart.legend.fit = function fit() {
            fitValue.bind(chart.legend)();
            return this.height += 20
        }
    }
}

// Config block
const cpuUtilConfig = {
    // Chart Type
    type: 'line',
    data: cpuUtilData,
    options: {
        /*
        Disable Aspect Ratio and enable setting the height of the canvas
        using CSS
        */
        maintainAspectRatio: false,
        plugins: {
            legend: {
                onClick: null,  // Disable click event on legend
                position: 'top',  // Position of the legend
                labels: {
                    // This more specific font property overrides the global property
                    font: {
                        size: 13
                    }
                }
            },  // End Legend
        },  // End Plugins
        scales: {
            x: {
                parsing: false,
                type: 'time',
                time: {
                    unit: 'day'
                },
                title: {
                    display: false,
                    text: 'Time',
                    font: {
                        size: 15
                    },
                    padding: {left: 0, top: 15, right: 0, bottom: 0},
                },
            },  // End x axis
            y: {
                min: 0,
                max: 100,
                ticks: {
                        callback: function(value, index, values) {
                                return value + '%';
                        }
                },
                title: {
                    display: false,
                    text: 'Utilization',
                    font: {
                        size: 15
                    },
                    padding: {left: 0, top: 0, right: 0, bottom: 15},
                }
            }  // End y axis
        }  // End scales
    },  // End options
    plugins: [cpuUtilLegendMargin]  // Add Legend Margin block
};  // End config


// render / init block
const cpuUtilChart = new Chart(
    document.getElementById('cpuutilizationchart'),
    cpuUtilConfig
)  // End Chart

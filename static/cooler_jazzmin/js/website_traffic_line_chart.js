// Setup block
const websiteTrafficData = {
    datasets: [{
        label: 'Active Users',
        // Chart Data
        data: users_line_chart_data,
        lineTension: 0.3,
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
    }]  // End datasets
};  // End data

// Legend Margin plugin block
const websiteTrafficLegendMargin = {
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
const websiteTrafficConfig = {
    // Chart Type
    type: 'line',
    data: websiteTrafficData,
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
            // Reformat dates in the tooltips
            tooltip: {
                callbacks: {
                    title: context => {
                    const d = new Date(context[0].raw.x);
                    const formattedDate = d.toLocaleString([], {
                    year: 'numeric', month: 'short', day: 'numeric'
                });
                return formattedDate
                    }  // End context
                }  // End callbacks
            }  // End ToolTip
        },  // End Plugins
        scales: {
            x: {
                parsing: false,
                type: 'time',
                // Set level of time in the x axis
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
                }
            },  // End x axis
            y: {
                // Begin y axis from zero
                beginAtZero: true,
                title: {
                    display: false,
                    text: 'Active users',
                    font: {
                        size: 15
                    },
                    padding: {left: 0, top: 0, right: 0, bottom: 15},
                }
            }  // End y axis
        }  // End scales
    },  // End options
    plugins: [websiteTrafficLegendMargin]  // Add Legend Margin block
};  // End config


// render / init block
const websiteTrafficChart = new Chart(
    document.getElementById('websiteTrafficLineChart'),
    websiteTrafficConfig
)  // End Chart

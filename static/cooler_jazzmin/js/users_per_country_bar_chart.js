// Setup block
const countryTrafficData = {
    labels: users_country_labels,
    datasets: [{
        label: 'Active Users',
        // Chart Data
        data: users_country_data,
        backgroundColor: ['#3C87D5', ],
        borderWidth: 1
    }]  // End datasets
};  // End data

// Legend Margin plugin block
const countryTrafficLegendMargin = {
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
const countryTrafficConfig = {
    // Chart Type
    type: 'bar',
    data: countryTrafficData,
    options: {
        indexAxis: 'x',
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
        },  // End Plugins
        scales: {
            x: {
                beginAtZero: true,
                ticks: {
                    autoSkip: false,
                    beginAtZero: true,
                    stepSize: 1,
                    maxRotation: 90,
                    minRotation: 0
                },
                title: {
                    display: false,
                    text: 'Countries',
                    font: {
                        size: 15
                    },
                    padding: {left: 0, top: 15, right: 0, bottom: 0},
                }
            },
            y: {
                title: {
                    display: false,
                    text: 'Active Users',
                    font: {
                        size: 15
                    },
                    padding: {left: 0, top: 0, right: 0, bottom: 15},
                }
            }
        }
    },  // End options
    plugins: [countryTrafficLegendMargin]  // Add Legend Margin block
};  // End config


// render / init block
const countryTrafficChart = new Chart(
    document.getElementById('userspercountrychart'),
    countryTrafficConfig
)  // End Chart

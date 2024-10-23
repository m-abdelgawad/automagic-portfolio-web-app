// Setup block
const pagesTrafficData = {
    // Chart Labels
    labels: users_page_labels,
    // Chart Datasets
    datasets: [{
        label: 'Active Users',
        backgroundColor: ['#3C87D5', ],
        data: users_page_data,
        borderWidth: 1
    }]  // End datasets
};  // End data

// Legend Margin plugin block
const pagesTrafficLegendMargin = {
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
const pagesTrafficConfig = {
    // Chart Type
    type: 'bar',
    // Chart Data
    data: pagesTrafficData,
    // Chart Options
    options: {
        // Set the index axis to Y
        indexAxis: 'y',
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
        },  // End Plugins
        scales: {
            x: {
                title: {
                    display: false,
                    text: 'Active Users',
                    font: {
                        size: 15
                    },
                    padding: {left: 0, top: 15, right: 0, bottom: 0},
                }
            },
            y: {
                // Begin y axis from zero
                beginAtZero: true,
                ticks: {
                    // Don't skip any Y labels
                    autoSkip: false,
                },
                title: {
                    display: false,
                    text: 'Page Title',
                    font: {
                        size: 15
                    },
                    padding: {left: 0, top: 0, right: 0, bottom: 15},
                }
            },
        }  // End scales
    },  // End options
    plugins: [pagesTrafficLegendMargin]  // Add Legend Margin block
};  // End config


// render / init block
const pagesTrafficChart = new Chart(
    document.getElementById('usersperpagechart'),
    pagesTrafficConfig
)  // End Chart

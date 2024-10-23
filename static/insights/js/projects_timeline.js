// Setup block
const projectsTimelineData = {
    datasets: [{
        label: 'Completed Projects',
        // Chart Data
        data: projects_timeline_chart_data,
        lineTension: 0.3,
        backgroundColor: ['#E8791E', ],
        borderColor: ['#E8791E', ],
        pointRadius: 3,
        pointBackgroundColor: ['#E8791E', ],
        pointBorderColor: ['#E8791E', ],
        pointHoverRadius: 3,
        pointHoverBackgroundColor: ['#E8791E', ],
        pointHoverBorderColor: ['#E8791E', ],
        pointHitRadius: 10,
        pointBorderWidth: 2,
    }]  // End datasets
};  // End data

// Legend Margin plugin block
const projectsTimelineLegendMargin = {
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
const projectsTimelineConfig = {
    // Chart Type
    type: 'line',
    data: projectsTimelineData,
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
            },  // End Legend
            // Reformat dates in the tooltips
            tooltip: {
                callbacks: {
                    title: context => {
                    const d = new Date(context[0].raw.x);
                    const formattedDate = d.toLocaleString([], {
                    year: 'numeric', month: 'short'
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
                    unit: 'month'
                }
            },  // End x axis
            y: {
                // Begin y axis from zero
                beginAtZero: true,
                ticks: {
                    stepSize: 1
                }
            }  // End y axis
        }  // End scales
    },  // End options
    plugins: [projectsTimelineLegendMargin]  // Add Legend Margin block
};  // End config


// render / init block
const projectsTimelineChart = new Chart(
    document.getElementById('projectsTimeline'),
    projectsTimelineConfig
)  // End Chart


// Setup block
const projectsSkillsData = {
    // Chart Labels
    labels: skills_labels,
    // Chart Datasets
    datasets: [{
        label: 'Projects',
        backgroundColor: ['#E8791E', ],
        data: skills_data,
        borderWidth: 1,
    }]  // End datasets
};  // End data

// Legend Margin plugin block
const projectsSkillsLegendMargin = {
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
const projectsSkillsConfig = {
    // Chart Type
    type: 'bar',
    // Chart Data
    data: projectsSkillsData,
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
            },  // End Legend
            // Reformat dates in the tooltips
        },  // End Plugins
        scales: {
            y: {
                // Begin y axis from zero
                beginAtZero: true,
                ticks: {
                    // Don't skip any Y labels
                    autoSkip: false,
                    // Begin y axis from zero
                    beginAtZero: true
            }
            },
            x: {
                ticks: {
                    stepSize: 1
                }
            }
        }  // End scales
    },  // End options
    plugins: [projectsSkillsLegendMargin]  // Add Legend Margin block
};  // End config


// render / init block
const projectsSkillsChart = new Chart(
    document.getElementById('ProjectsSkills'),
    projectsSkillsConfig
)  // End Chart

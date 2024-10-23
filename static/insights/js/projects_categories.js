// Setup block
const projectsCategoriesData = {
    // Chart Labels
    labels: projects_categories_labels,
    // Chart Datasets
    datasets: [{
        label: 'Projects',
        data: projects_categories_data,
        backgroundColor: ['#E8791E', '#FF5722', '#E64E1F', '#CC461B', '#B33D18', '#993414', '#802C11', '#66230E', '#4D1A0A', ],
        borderWidth: 1
    }]  // End datasets
};  // End data

// Legend Margin plugin block
const projectsCategoriesLegendMargin = {
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
const projectsCategoriesConfig = {
    // Chart Type
    type: 'doughnut',
    // Chart Data
    data: projectsCategoriesData,
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
        // Doughnut gap size
        // cutout: 70,
    },  // End options
    plugins: [projectsCategoriesLegendMargin]  // Add Legend Margin block
};  // End config


// render / init block
const projectsCategoriesChart = new Chart(
    document.getElementById('projectsCategories'),
    projectsCategoriesConfig
)  // End Chart

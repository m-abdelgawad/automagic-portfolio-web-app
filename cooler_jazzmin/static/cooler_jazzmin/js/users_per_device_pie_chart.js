// Setup block
const devicesTrafficData = {
    // Chart Labels
    labels: users_device_labels,
    // Chart Datasets
    datasets: [{
        label: 'Active Users',
        data: users_device_data,
        backgroundColor: ['#3C87D5', '#2f619d', '#3368ac', '#487ab9', '#5d7abe', '#4c80c9', '#3c87d5', '#9bacd3', '#dee8f0', ],
        borderWidth: 1
    }]  // End datasets
};  // End data

// Legend Margin plugin block
const devicesTrafficLegendMargin = {
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
const devicesTrafficConfig = {
    // Chart Type
    type: 'doughnut',
    // Chart Data
    data: devicesTrafficData,
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
    plugins: [devicesTrafficLegendMargin]  // Add Legend Margin block
};  // End config


// render / init block
const devicesTrafficChart = new Chart(
    document.getElementById('usersperdevicechart'),
    devicesTrafficConfig
)  // End Chart

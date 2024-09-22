<script>
	import BarChart from './BarChart.svelte';
    import LineChart from './LineChart.svelte';
    import PieChart from './PieChart.svelte';
    import ScatterPlot from './ScatterPlot.svelte';

    let barData = [10, 20, 30, 40, 50];
    let lineData = [
        { year: 2015, value: 30 },
        { year: 2016, value: 50 },
        { year: 2017, value: 40 },
        { year: 2018, value: 70 },
        { year: 2019, value: 60 }
    ];
    let pieData = [
        { crop: "Milho", value: 40 },
        { crop: "Soja", value: 30 },
        { crop: "Trigo", value: 20 },
        { crop: "Algodão", value: 10 }
    ];
    let scatterData = [
        { temperature: 20, production: 50 },
        { temperature: 25, production: 80 },
        { temperature: 30, production: 60 },
        { temperature: 35, production: 100 },
        { temperature: 40, production: 90 }
    ];
</script>

<main>
	<h1>Dashboard</h1>
    
    <h2>Produção por Tipo de Cultivo</h2>
    <BarChart {barData} />

    <h2>Produtividade ao Longo dos Anos</h2>
    <LineChart {lineData} />

    <h2>Proporção de Cultivos</h2>
    <PieChart {pieData} />

    <h2>Correlação Temperatura x Produção</h2>
    <ScatterPlot {scatterData} />
</main>

<style>
	main {
        font-family: Arial, sans-serif;
        margin: 20px;
    }
    h1 {
        color: #ff6600;
        text-align: center;
    }
    h2 {
        color: #333;
    }
</style>
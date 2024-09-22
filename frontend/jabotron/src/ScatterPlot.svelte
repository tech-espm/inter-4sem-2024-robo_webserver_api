<script>
    import { onMount } from "svelte";
    import * as d3 from "d3";

    export let scatterData = [];

    let chart;
    let width = 500;
    let height = 300;
    let margin = { top: 20, right: 30, bottom: 40, left: 40 };

    onMount(() => {
        const svg = d3.select(chart)
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        const x = d3.scaleLinear()
            .domain([d3.min(scatterData, d => d.temperature), d3.max(scatterData, d => d.temperature)])
            .range([0, width - margin.left - margin.right]);

        const y = d3.scaleLinear()
            .domain([0, d3.max(scatterData, d => d.production)])
            .range([height - margin.top - margin.bottom, 0]);

        svg.append("g")
            .attr("transform", `translate(0,${height - margin.top - margin.bottom})`)
            .call(d3.axisBottom(x));

        svg.append("g")
            .call(d3.axisLeft(y));

        svg.selectAll("circle")
            .data(scatterData)
            .enter()
            .append("circle")
            .attr("cx", d => x(d.temperature))
            .attr("cy", d => y(d.production))
            .attr("r", 0)
            .attr("fill", "#ff6600")
            .transition()
            .duration(1000)
            .attr("r", 6);
    });
</script>

<svg bind:this={chart}></svg>

<style>
    svg {
        display: block;
        margin: auto;
    }
    circle:hover {
        fill: #ffa500;
    }
</style>

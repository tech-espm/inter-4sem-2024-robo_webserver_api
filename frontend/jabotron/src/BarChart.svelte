<script>
    import { onMount } from "svelte";
    import * as d3 from "d3";

    export let data = [10, 20, 30, 40, 50]; 

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

        const x = d3.scaleBand()
            .domain(d3.range(data.length))
            .range([0, width - margin.left - margin.right])
            .padding(0.1);

        const y = d3.scaleLinear()
            .domain([0, d3.max(data)])
            .range([height - margin.top - margin.bottom, 0]);

        // Eixos
        svg.append("g")
            .attr("transform", `translate(0,${height - margin.top - margin.bottom})`)
            .call(d3.axisBottom(x).tickFormat(i => i + 1).tickSizeOuter(0));

        svg.append("g")
            .call(d3.axisLeft(y));

        // Barras
        svg.selectAll("rect")
            .data(data)
            .enter()
            .append("rect")
            .attr("x", (d, i) => x(i))
            .attr("y", d => y(0))
            .attr("width", x.bandwidth())
            .attr("height", 0)
            .attr("fill", "#ff6600")
            .transition()
            .duration(800)
            .attr("y", d => y(d))
            .attr("height", d => y(0) - y(d));
    });
</script>

<svg bind:this={chart}></svg>

<style>
    svg {
        display: block;
        margin: auto;
    }
    rect:hover {
        fill: #ffa500;
    }
</style>

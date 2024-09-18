<script>
    import { onMount } from "svelte";
    import * as d3 from "d3";

    export let lineData = [];

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
            .domain([d3.min(lineData, d => d.year), d3.max(lineData, d => d.year)])
            .range([0, width - margin.left - margin.right]);

        const y = d3.scaleLinear()
            .domain([0, d3.max(lineData, d => d.value)])
            .range([height - margin.top - margin.bottom, 0]);

        const line = d3.line()
            .x(d => x(d.year))
            .y(d => y(d.value));

        svg.append("g")
            .attr("transform", `translate(0,${height - margin.top - margin.bottom})`)
            .call(d3.axisBottom(x).ticks(5).tickFormat(d3.format("d")));

        svg.append("g")
            .call(d3.axisLeft(y));

        // Linha
        svg.append("path")
            .datum(lineData)
            .attr("fill", "none")
            .attr("stroke", "#ff6600")
            .attr("stroke-width", 2)
            .attr("d", line)
            .attr("stroke-dasharray", function() {
                const totalLength = this.getTotalLength();
                return `${totalLength} ${totalLength}`;
            })
            .attr("stroke-dashoffset", function() {
                return this.getTotalLength();
            })
            .transition()
            .duration(2000)
            .attr("stroke-dashoffset", 0);
    });
</script>

<svg bind:this={chart}></svg>

<style>
    svg {
        display: block;
        margin: auto;
    }
</style>

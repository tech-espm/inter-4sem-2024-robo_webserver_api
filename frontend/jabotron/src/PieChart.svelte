<script>
    import { onMount } from "svelte";
    import * as d3 from "d3";

    export let pieData = [];

    let chart;
    let width = 300;
    let height = 300;
    let radius = Math.min(width, height) / 2;

    onMount(() => {
        const svg = d3.select(chart)
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", `translate(${width / 2},${height / 2})`);

        const color = d3.scaleOrdinal()
            .domain(pieData.map(d => d.crop))
            .range(d3.schemeCategory10);

        const pie = d3.pie()
            .value(d => d.value)
            .sort(null);

        const arc = d3.arc()
            .innerRadius(0)
            .outerRadius(radius);

        svg.selectAll("path")
            .data(pie(pieData))
            .enter()
            .append("path")
            .attr("d", arc)
            .attr("fill", d => color(d.data.crop))
            .transition()
            .duration(1000)
            .attrTween("d", function(d) {
                const i = d3.interpolate({ startAngle: 0, endAngle: 0 }, d);
                return t => arc(i(t));
            });
    });
</script>

<svg bind:this={chart}></svg>

<style>
    svg {
        display: block;
        margin: auto;
    }
</style>

<!--
Created using JS Bin
http://jsbin.com

Copyright (c) 2024 by anonymous (http://jsbin.com/letopiqipi/1/edit)

Released under the MIT license: http://jsbin.mit-license.org
-->
<meta name="robots" content="noindex">

<script id="jsbin-javascript">
const power = (x, n) => {
    if (n === 0) return 1;
    let result = x;
    for (let i = 1; i < n; i++) {
        result *= x;
    }
    return result;
};
</script>
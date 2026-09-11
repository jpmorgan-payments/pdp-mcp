from jpmc.mcp_for_api_documentation.util import extract_content_from_html


def test_extract_content_from_html_strips_nav_and_keeps_body():
    html = """
    <html><head><title>Test</title></head>
    <body>
    <div id="main-content">
      <nav>skip me</nav>
      <h1>Payments API</h1>
      <p>This is the <b>real</b> content.</p>
      <div class="doc-cookie-banner">cookie notice</div>
      <a href="/x">link</a>
      <noscript>no js</noscript>
    </div>
    </body></html>
    """

    result = extract_content_from_html(html)

    assert "real" in result
    assert "skip me" not in result
    assert "cookie notice" not in result
    assert "no js" not in result


def test_extract_content_from_html_empty_input():
    assert extract_content_from_html("") == "<e>Empty HTML content</e>"

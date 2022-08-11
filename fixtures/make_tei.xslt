<xsl:stylesheet xmlns="http://www.tei-c.org/ns/1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs tei" version="1.0">
    <xsl:param name="file_name"/>
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="tei:fw"/>
    <xsl:template match="tei:lb[not(@break='paragraph')]"/>
    <xsl:template match="tei:lb[@break='paragraph']">
        <xsl:text>&#160;</xsl:text>
    </xsl:template>
    <xsl:template match="tei:pb"/>
    <xsl:template match="tei:hi">
        <xsl:apply-templates/>
    </xsl:template>

</xsl:stylesheet>

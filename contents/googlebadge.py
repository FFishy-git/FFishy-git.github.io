import gsbg

article_link = "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=j9qvUg0AAAAJ&citation_for_view=j9qvUg0AAAAJ:Y0pCki6q_DkC"
profile_link = "https://scholar.google.com/citations?user=S1tCv5MAAAAJ&hl=en"

article_citation_num = gsbg.fetch_article_citation_num(article_link)
profile_citation_num = gsbg.fetch_profile_citation_num(profile_link)
gsbg.gene_citation_badge_link(
    link=profile_link, 
    link_type="profile",
)
gsbg.gene_citation_badge_svg(
    link=profile_link, 
    link_type="profile",
    svg_name='gsbg.svg',
    path_to_save='generated_badges',
)
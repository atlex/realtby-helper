package org.am.realtby;

import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * @author Alexander Maximenya
 * @version 2013-03-11
 */
public class Parser {
    protected Connection connection;
    protected String url;
    protected File file;

    public Parser(File file) {
        this.file = file;
    }

    public Parser(String url) {
        this.url = url;
    }

    protected Document connect() throws IOException {
        if (url != null) {
            if (connection == null) {
                connection = Jsoup.connect(url);
                connection.userAgent("0");
            }
            return connection.get();
        } else if (file != null) {
            return Jsoup.parse(file, "UTF-8");
        }
        return null;
    }

    public List<Offer> getOffers() throws IOException {
        Document doc = connect();
        List<Offer> offers = new ArrayList<Offer>();

        Elements specialOffersTable = doc.select("#photolist");
        if (specialOffersTable != null) {
            Elements specialOffersRows = specialOffersTable.select(".row");
            if (specialOffersRows != null) {
                for (Element specialOfferRow: specialOffersRows) {
                    Offer offer = new Offer();

                    Element thumbnail = specialOfferRow.select(".thumb-frame").first();
                    if (thumbnail != null) {
                        Element url = thumbnail.select("a").first();
                        if (url != null) {
                            offer.setUrl(url.attr("href"));
                        }
                    }

                    Elements descriptions = specialOfferRow.select(".max150");
                    if (descriptions != null) {
                        for (Element description : descriptions) {
                            offer.setDescription(description.text());
                        }
                    }
                    offers.add(offer);
                }
            }
        }
        return offers;
    }
}

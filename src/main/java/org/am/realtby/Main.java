package org.am.realtby;

import org.jsoup.Connection;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.File;
import java.io.IOException;
import java.util.List;

/**
 * @author Alexander Maximenya
 * @version 2013-03-05
 */
public class Main {

    public static void main(String[] args) {
        try {
            parseSpecialOffersTable();
        } catch (IOException e) {
            e.printStackTrace();
        }


//        try {
//            Connection conn = Jsoup.connect("http://realt.by/sale/flats/category/3");
//            conn.userAgent("0");
//            Document doc = conn.get();
//
//
//            Elements specialOffersTable = doc.select("#photolist");
//            if (specialOffersTable != null) {
//                Elements specialOffersRows = specialOffersTable.select(".row");
//                if (specialOffersRows != null) {
//                    for (Element specialOfferRow: specialOffersRows) {
//                        System.out.println(specialOfferRow);
//                    }
//                }
//            }
////            System.out.println(specialOffersTable);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }

    }

    protected static void parseSpecialOffersTable() throws IOException {
        File file = new File("specialOffersTable.html");
        Parser parser = new Parser(file);
        List<Offer> offers = parser.getOffers();
        if (offers != null) {
            for (Offer offer : offers) {
                System.out.println(offer.toString());
                System.out.println("---------------------------------------\n");
            }
        }
    }


}

package org.am.realtby;

/**
 * @author Alexander Maximenya
 * @version 2013-03-11
 */
public class Offer {
    protected String url;
    protected String description;

    public Offer() {
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @Override
    public String toString() {
        return "Offer{" +
                "url='" + url + '\'' +
                ", description='" + description + '\'' +
                '}';
    }
}

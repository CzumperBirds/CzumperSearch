package com.czumpers.data_processor.kafka.model;

import lombok.Data;
import lombok.EqualsAndHashCode;

import java.util.List;
import java.util.Map;

@Data
@EqualsAndHashCode(of = {"title", "link", "author", "published"})
public class DailyTriviaConsumed {
    private String title;
    private String link;
    private String author;
    private String published;
    private List<Map<String, String>> tags;
}

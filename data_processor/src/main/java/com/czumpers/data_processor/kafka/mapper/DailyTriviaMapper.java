package com.czumpers.data_processor.kafka.mapper;

import com.czumpers.data_processor.kafka.model.DailyTriviaConsumed;
import com.czumpers.data_processor.kafka.model.ResourceProduced;
import org.springframework.stereotype.Component;

import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Component
public class DailyTriviaMapper {
    private static final String DEFAULT_TYPE = "trivia";
    private static final String DEFAULT_SOURCE = "daily trivia";
    private static final List<String> DEFAULT_TAGS = List.of(
            "daily", "trivia", "fun facts", "random facts", "interesting facts",
            "did you know", "TIL", "trivia of the day", "mind-blowing facts",
            "cool facts", "surprising facts"
    );

    public ResourceProduced mapToResource(DailyTriviaConsumed consumed) {
        ResourceProduced produced = new ResourceProduced();
        produced.setType(DEFAULT_TYPE);
        produced.setSource(DEFAULT_SOURCE);
        produced.setTags(DEFAULT_TAGS);
        produced.setContent(consumed.getTitle());
        produced.setPublished(formatPublishedDate(consumed.getPublished()));
        return produced;
    }

    private String formatPublishedDate(String published) {
        OffsetDateTime dateTime = OffsetDateTime.parse(published);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        return dateTime.format(formatter);
    }
}

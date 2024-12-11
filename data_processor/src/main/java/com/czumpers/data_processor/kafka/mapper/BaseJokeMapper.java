package com.czumpers.data_processor.kafka.mapper;

import com.czumpers.data_processor.kafka.model.ResourceProduced;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

public abstract class BaseJokeMapper<T> {
    private static final Map<String, List<String>> FLAGS_DICTIONARY = new HashMap<>() {{
        put("nsfw", Arrays.asList("adult", "mature", "explicit", "18+", "inappropriate"));
        put("religious", Arrays.asList("god", "faith", "church", "spiritual", "prayer"));
        put("political", Arrays.asList("politics", "government", "election", "republican", "democrat"));
        put("racist", Arrays.asList("racism", "prejudice", "discrimination", "equality", "racism jokes"));
        put("sexist", Arrays.asList("gender inequality", "sexism", "misogyny", "feminism", "gender jokes"));
        put("explicit", Arrays.asList("adult", "explicit content", "offensive", "mature humor", "dark humor"));
    }};

    protected abstract String getType();
    protected abstract String getSource();
    protected abstract String getContent(T consumed);
    protected abstract Map<String, Boolean> getFlags(T consumed);
    protected abstract String getCategory(T consumed);

    public ResourceProduced mapToResource(T consumed) {
        ResourceProduced produced = new ResourceProduced();
        produced.setType(getType());
        produced.setSource(getSource());
        produced.setContent(getContent(consumed));
        produced.setPublished(getDateTime());
        produced.setTags(getTags(consumed));
        return produced;
    }

    private String getDateTime() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        return LocalDateTime.now().format(formatter);
    }

    private List<String> getTags(T consumed) {
        List<String> tags = new ArrayList<>();

        Map<String, Boolean> flags = getFlags(consumed);
        for (Map.Entry<String, Boolean> entry : flags.entrySet()) {
            if (entry.getValue()) {
                List<String> flagTags = FLAGS_DICTIONARY.get(entry.getKey());
                if (flagTags != null) {
                    tags.addAll(flagTags);
                }
            }
        }

        String category = getCategory(consumed);
        if (category != null && !category.isEmpty()) {
            tags.add(category);
        }

        return tags;
    }
}
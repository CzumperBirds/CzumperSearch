package com.czumpers.data_processor.kafka.mapper;

import com.czumpers.data_processor.kafka.model.OnePartJokeConsumed;
import org.springframework.stereotype.Component;

import java.util.Map;

@Component
public class OnePartJokeMapper extends BaseJokeMapper<OnePartJokeConsumed> {
    private static final String DEFAULT_TYPE = "joke";
    private static final String DEFAULT_SOURCE = "one part jokes";

    @Override
    protected String getType() {
        return DEFAULT_TYPE;
    }

    @Override
    protected String getSource() {
        return DEFAULT_SOURCE;
    }

    @Override
    protected String getContent(OnePartJokeConsumed consumed) {
        return consumed.getJoke();
    }

    @Override
    protected Map<String, Boolean> getFlags(OnePartJokeConsumed consumed) {
        return consumed.getFlags();
    }

    @Override
    protected String getCategory(OnePartJokeConsumed consumed) {
        return consumed.getCategory();
    }
}
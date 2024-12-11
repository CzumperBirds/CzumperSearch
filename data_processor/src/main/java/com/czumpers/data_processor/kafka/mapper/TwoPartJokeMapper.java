package com.czumpers.data_processor.kafka.mapper;

import com.czumpers.data_processor.kafka.model.TwoPartJokeConsumed;
import org.springframework.stereotype.Component;

import java.util.Map;

@Component
public class TwoPartJokeMapper extends BaseJokeMapper<TwoPartJokeConsumed> {
    private static final String DEFAULT_TYPE = "joke";
    private static final String DEFAULT_SOURCE = "two part jokes";

    @Override
    protected String getType() {
        return DEFAULT_TYPE;
    }

    @Override
    protected String getSource() {
        return DEFAULT_SOURCE;
    }

    @Override
    protected String getContent(TwoPartJokeConsumed consumed) {
        return consumed.getSetup() + "\n" + consumed.getDelivery();
    }

    @Override
    protected Map<String, Boolean> getFlags(TwoPartJokeConsumed consumed) {
        return consumed.getFlags();
    }

    @Override
    protected String getCategory(TwoPartJokeConsumed consumed) {
        return consumed.getCategory();
    }
}
package com.czumpers.data_processor.kafka.consumer;

import com.czumpers.data_processor.kafka.model.TwoPartJokeConsumed;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Slf4j
@Service
public class TwoPartJokeConsumer {

    @KafkaListener(
            topics = "two-part-jokes",
            groupId = "spring-middleman",
            properties = {"spring.json.value.default.type=com.czumpers.data_processor.kafka.model.TwoPartJokeConsumed"}
    )
    public void consume(TwoPartJokeConsumed joke) {
        log.info("#### -> Two part joke consumed -> {}", joke);
    }
}
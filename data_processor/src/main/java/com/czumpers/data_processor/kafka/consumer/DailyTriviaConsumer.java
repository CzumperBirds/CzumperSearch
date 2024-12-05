package com.czumpers.data_processor.kafka.consumer;

import com.czumpers.data_processor.kafka.model.DailyTriviaConsumed;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Slf4j
@Service
public class DailyTriviaConsumer {

    @KafkaListener(
            topics = "daily-trivia",
            groupId = "spring-middleman",
            properties = {"spring.json.value.default.type=com.czumpers.data_processor.kafka.model.DailyTriviaConsumed"}
    )
    public void consume(DailyTriviaConsumed trivia) {
        log.info("#### -> Daily trivia consumed -> {}", trivia);
    }
}

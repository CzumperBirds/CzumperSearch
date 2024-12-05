package com.czumpers.data_processor.kafka.consumer;

import com.czumpers.data_processor.kafka.model.OnePartJokeConsumed;
import com.czumpers.data_processor.mongo.service.OnePartJokeService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Slf4j
@Service
@RequiredArgsConstructor
public class OnePartJokeConsumer {

    private final OnePartJokeService onePartJokeService;

    @KafkaListener(
            topics = "one-part-jokes",
            groupId = "spring-middleman",
            properties = {"spring.json.value.default.type=com.czumpers.data_processor.kafka.model.OnePartJokeConsumed"}
    )
    public void consume(OnePartJokeConsumed joke) {
        log.info("#### -> One part joke consumed -> {}", joke);
        if (onePartJokeService.isNewJoke(joke)) {
            onePartJokeService.saveJoke(joke);
            log.info("#### -> New one part joke saved");
        } else {
            log.info("#### -> Duplicate one part joke");
        }
    }
}
